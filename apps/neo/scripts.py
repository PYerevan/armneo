from py2neo import Node, RelationshipMatcher, Relationship, NodeMatcher
from apps.neo.models import graph


def get_or_create_node(label, **properties):
    created = False
    matcher = NodeMatcher(graph)
    node = matcher.match(label, **properties).first()
    if not node:
        node = Node(label, **properties)
        graph.create(node)
        created = True
    return node, created


def get_or_create_relationship(start_node, relationship_type, end_node, **properties):
    created = False
    matcher = RelationshipMatcher(graph)
    relationship = matcher.match(nodes=[start_node, end_node], r_type=relationship_type)
    if not relationship.exists():
        created = True
        relationship = graph.create(Relationship(start_node, relationship_type, end_node, **properties))
    return created, relationship
