import graphene

from RoomBooker.schema import Query as RoomQuery


class Query(RoomQuery, graphene.ObjectType):
    # Top level Query
    pass


schema = graphene.Schema(query=Query)
