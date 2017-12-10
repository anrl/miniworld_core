from miniworld.model.Objects import Objects
from miniworld.singletons import singletons


class EmulationNodes(Objects):
    def filter_real_emulation_nodes(self):
        """
        Return all nodes which belong to a real emulation (therefore belong to a qemu instance).

        Returns
        -------
        EmulationNodes
        """

        from miniworld.nodes.virtual.VirtualNode import VirtualNode
        return self.filter_type(fun=lambda node: not isinstance(node, VirtualNode))

    def filter_central_nodes(self):
        """

        Returns
        -------
        list<CentralNode>
        """

        from miniworld.nodes.virtual.CentralNode import CentralNode
        return self.filter_type(fun=CentralNode.is_central_node)

    def filter_mgmt_nodes(self):
        """

        Returns
        -------
        list<ManagementNode>
        """
        from miniworld.nodes.virtual.CentralNode import CentralNode
        return self.filter_type(fun=CentralNode.is_management_node)

    def sort_by_locality(self):
        """
        Assume there are 2 nodes in the list. Return the local node first in a new :py:class:`.EmulationNodes` object.

        Returns
        -------
        EmulationNodes
        """
        if len(self) != 2:
            raise ValueError("Only supported for 2 nodes!")

        emulation_node_x, emulation_node_y = self

        if singletons.simulation_manager.is_connection_among_servers(emulation_node_x, emulation_node_y):

            # one of both must be local
            if singletons.simulation_manager.is_local_node(emulation_node_x._node._id):
                return EmulationNodes([emulation_node_x, emulation_node_y])

            return EmulationNodes([emulation_node_y, emulation_node_x])

        return self
