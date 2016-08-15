import korean
from django.test import TestCase


# Create your tests here.

class TemplateKoreanTestCase(TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        self.assertTrue(0 == 0)
        self.assertEquals(1, 1)

    def test_korean_proofread(self):
        result = korean.l10n.proofread("나(은)는 사람이다.")
        self.assertEqual("나는 사람이다.", result)

    def test_korean_proofread_fail(self):
        result = korean.l10n.proofread("나(은)는 사람이다.")
        self.assertNotEqual(u"나은 사람이다.", result)

    def test_korean_proofread_Tag(self):
        from django.template import Context, Template
        rendered = Template(
            '{% load proofread %}'
            '{{ string|proofread }}'
        ).render(Context({
            'string': '나(은)는 밥(을)를 먹었다.',
        }))
        self.assertEqual(rendered, '나는 밥을 먹었다.')
