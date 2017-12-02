# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestNodes.test_node_interfaces 1'] = {
    'data': {
        'emulationNodes': [
            {
                'id': 'RW11bGF0aW9uTm9kZTow',
                'iid': 0,
                'interfaces': {
                    'edges': [
                        {
                            'node': {
                                'id': 'SW50ZXJmYWNlOjA=',
                                'iid': 0,
                                'ipv4': '10.0.1.1',
                                'kind': None,
                                'mac': '02:01:00:00:00:00',
                                'name': 'mesh'
                            }
                        },
                        {
                            'node': {
                                'id': 'SW50ZXJmYWNlOjE=',
                                'iid': 1,
                                'ipv4': '172.21.0.1',
                                'kind': None,
                                'mac': '0a:01:00:00:00:00',
                                'name': 'management'
                            }
                        }
                    ]
                },
                'virtualization': 'QemuTap'
            },
            {
                'id': 'RW11bGF0aW9uTm9kZTox',
                'iid': 1,
                'interfaces': {
                    'edges': [
                        {
                            'node': {
                                'id': 'SW50ZXJmYWNlOjI=',
                                'iid': 2,
                                'ipv4': '10.0.1.2',
                                'kind': None,
                                'mac': '02:01:00:00:00:01',
                                'name': 'mesh'
                            }
                        },
                        {
                            'node': {
                                'id': 'SW50ZXJmYWNlOjM=',
                                'iid': 3,
                                'ipv4': '172.21.0.2',
                                'kind': None,
                                'mac': '0a:01:00:00:00:01',
                                'name': 'management'
                            }
                        }
                    ]
                },
                'virtualization': 'QemuTap'
            }
        ]
    }
}

snapshots['TestNodes.test_node_distances[3] 1'] = {
    'data': {
        'emulationNodes': [
            {
                'distances': {
                    'edges': [
                        {
                            'node': {
                                'distance': 1.0,
                                'emulationNode': {
                                    'id': 'RW11bGF0aW9uTm9kZTox',
                                    'iid': 1
                                }
                            }
                        }
                    ]
                },
                'iid': 0
            },
            {
                'distances': {
                    'edges': [
                        {
                            'node': {
                                'distance': 1.0,
                                'emulationNode': {
                                    'id': 'RW11bGF0aW9uTm9kZToy',
                                    'iid': 2
                                }
                            }
                        }
                    ]
                },
                'iid': 1
            },
            {
                'distances': {
                    'edges': [
                    ]
                },
                'iid': 2
            }
        ]
    }
}

snapshots['TestNodes.test_node_links[3] 1'] = {
    'data': {
        'emulationNodes': [
            {
                'iid': 0,
                'links': {
                    'edges': [
                        {
                            'node': {
                                'connected': True,
                                'id': 'Q29ubmVjdGlvbjow',
                                'iid': 0,
                                'impairment': {
                                    'bandwidth': 500,
                                    'loss': 0.5
                                },
                                'kind': 'user',
                                'other': {
                                    'emulationNode': {
                                        'iid': 1
                                    },
                                    'interface': {
                                        'iid': 2
                                    }
                                },
                                'this': {
                                    'interface': {
                                        'iid': 0
                                    }
                                }
                            }
                        },
                        {
                            'node': {
                                'connected': True,
                                'id': 'Q29ubmVjdGlvbjox',
                                'iid': 1,
                                'impairment': {
                                    'bandwidth': 500,
                                    'loss': 0.5
                                },
                                'kind': 'user',
                                'other': {
                                    'emulationNode': {
                                        'iid': 2
                                    },
                                    'interface': {
                                        'iid': 4
                                    }
                                },
                                'this': {
                                    'interface': {
                                        'iid': 2
                                    }
                                }
                            }
                        }
                    ]
                },
                'virtualization': 'QemuTap'
            },
            {
                'iid': 1,
                'links': {
                    'edges': [
                        {
                            'node': {
                                'connected': True,
                                'id': 'Q29ubmVjdGlvbjow',
                                'iid': 0,
                                'impairment': {
                                    'bandwidth': 500,
                                    'loss': 0.5
                                },
                                'kind': 'user',
                                'other': {
                                    'emulationNode': {
                                        'iid': 1
                                    },
                                    'interface': {
                                        'iid': 2
                                    }
                                },
                                'this': {
                                    'interface': {
                                        'iid': 0
                                    }
                                }
                            }
                        },
                        {
                            'node': {
                                'connected': True,
                                'id': 'Q29ubmVjdGlvbjox',
                                'iid': 1,
                                'impairment': {
                                    'bandwidth': 500,
                                    'loss': 0.5
                                },
                                'kind': 'user',
                                'other': {
                                    'emulationNode': {
                                        'iid': 2
                                    },
                                    'interface': {
                                        'iid': 4
                                    }
                                },
                                'this': {
                                    'interface': {
                                        'iid': 2
                                    }
                                }
                            }
                        }
                    ]
                },
                'virtualization': 'QemuTap'
            },
            {
                'iid': 2,
                'links': {
                    'edges': [
                        {
                            'node': {
                                'connected': True,
                                'id': 'Q29ubmVjdGlvbjow',
                                'iid': 0,
                                'impairment': {
                                    'bandwidth': 500,
                                    'loss': 0.5
                                },
                                'kind': 'user',
                                'other': {
                                    'emulationNode': {
                                        'iid': 1
                                    },
                                    'interface': {
                                        'iid': 2
                                    }
                                },
                                'this': {
                                    'interface': {
                                        'iid': 0
                                    }
                                }
                            }
                        },
                        {
                            'node': {
                                'connected': True,
                                'id': 'Q29ubmVjdGlvbjox',
                                'iid': 1,
                                'impairment': {
                                    'bandwidth': 500,
                                    'loss': 0.5
                                },
                                'kind': 'user',
                                'other': {
                                    'emulationNode': {
                                        'iid': 2
                                    },
                                    'interface': {
                                        'iid': 4
                                    }
                                },
                                'this': {
                                    'interface': {
                                        'iid': 2
                                    }
                                }
                            }
                        }
                    ]
                },
                'virtualization': 'QemuTap'
            }
        ]
    }
}

snapshots['TestNodes.test_node_id_filter 1'] = {
    'data': {
        'emulationNodes': [
            {
                'id': 'RW11bGF0aW9uTm9kZTow',
                'iid': 0
            }
        ]
    }
}

snapshots['TestNodes.test_node_get 1'] = {
    'data': {
        'node': {
            'id': 'RW11bGF0aW9uTm9kZTow',
            'iid': 0
        }
    }
}

snapshots['TestNodes.test_interface_get 1'] = {
    'data': {
        'node': {
            'id': 'SW50ZXJmYWNlOjA=',
            'iid': 0
        }
    }
}

snapshots['TestNodes.test_connection_get 1'] = {
    'data': {
        'node': {
            'id': 'Q29ubmVjdGlvbjow',
            'iid': 0
        }
    }
}
