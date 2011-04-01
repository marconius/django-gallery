from django.db.models import Manager

class CollectionManager(Manager):

    def live(self):
        return self.get_query_set().filter(live=1)

class PaintingManager(Manager):

    def live(self):
        return self.get_query_set().filter(live=1)

