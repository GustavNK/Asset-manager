import graphene
from graphene_django import DjangoObjectType

from . import models


class UserType(DjangoObjectType):
    class Meta:
        model = models.User
        fields = "__all__"


class OrganisationsType(DjangoObjectType):
    class Meta:
        model = models.Organisation
        fields = "__all__"


class RoomType(DjangoObjectType):
    class Meta:
        model = models.Room
        fields = "__all__"


class BookingType(DjangoObjectType):
    class Meta:
        model = models.Booking
        fields = "__all__"



class Query(graphene.ObjectType):
    all_organisations = graphene.List(OrganisationsType)

    def resolve_all_organisations(self, info):
        return models.Organisation.objects.all()


schema = graphene.Schema(query=Query)
