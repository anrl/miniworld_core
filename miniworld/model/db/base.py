import json

from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Enum

from miniworld.network.AbstractConnection import AbstractConnection

Base = declarative_base()


class StringyJSON(types.TypeDecorator):
    """Stores and retrieves JSON as TEXT."""

    impl = types.TEXT

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


MagicJSON = types.JSON().with_variant(StringyJSON, 'sqlite')


class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    interfaces = relationship('Interface', order_by='Interface.id', back_populates='node')

    @staticmethod
    def from_domain(node) -> 'Node':
        interfaces = []
        for interface in node.network_mixin.interfaces:
            interfaces.append(
                Interface.from_domain(node, interface)
            )
        db_node = Node(
            id=node._id,
            interfaces=interfaces
        )
        return db_node


class Interface(Base):
    __tablename__ = 'interfaces'

    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey('nodes.id'))
    node = relationship('Node', back_populates='interfaces')

    mac = Column(String, nullable=False, unique=True)
    ipv4 = Column(String, unique=True)
    ipv6 = Column(String, unique=True)

    @staticmethod
    def from_domain(node, interface) -> 'Interface':
        return Interface(
            id=interface._id,
            node_id=node._id,
            mac=interface.mac,
            ipv4=None,
            ipv6=None,
        )


class Connection(Base):
    __tablename__ = 'connections'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(AbstractConnection.ConnectionType), nullable=False, default=AbstractConnection.ConnectionType.user)

    interface_x_id = Column(Integer, ForeignKey('interfaces.id'))
    interface_x = relationship('Interface', foreign_keys=[interface_x_id])
    interface_y_id = Column(Integer, ForeignKey('interfaces.id'))
    interface_y = relationship('Interface', foreign_keys=[interface_y_id])

    node_x_id = Column(Integer, ForeignKey('nodes.id'))
    node_x = relationship('Node', foreign_keys=[node_x_id])
    node_y_id = Column(Integer, ForeignKey('nodes.id'))
    node_y = relationship('Node', foreign_keys=[node_y_id])

    impairment = Column(MagicJSON, nullable=False, default={})
    active = Column(Boolean, default=True, nullable=False)
    step_added = Column(Integer, nullable=False)

    @staticmethod
    def from_domain(connection) -> 'Connection':
        return Connection(
            node_x_id=connection.emulation_node_x._id,
            node_y_id=connection.emulation_node_y._id,
            interface_x_id=connection.interface_x._id,
            interface_y_id=connection.interface_y._id,
            type=connection.connection_type,
        )
