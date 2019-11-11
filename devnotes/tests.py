from django.test import TestCase
from devnotes.models import Devnote

class DevnoteTestCases(TestCase):
    def setUp(self):
        Devnote.objects.create(name='testnote',
                                            description='testnote description')

    def test_retrieve_note(self):
        """retrieve the testnote"""
        testnote=Devnote.objects.all()[0]
        self.assertEqual(testnote.name, 'testnote')

    def test_create_new_entry(self):
        """create new note"""
        new_note = Devnote.objects.create(name='newnote',
                                            description='newnote description')
        db_entry= Devnote.objects.order_by('-created_at')[0]
        self.assertEqual(new_note.name,db_entry.name)
