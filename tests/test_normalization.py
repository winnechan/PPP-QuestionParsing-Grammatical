import json

from ppp_questionparsing_grammatical import computeTree, simplify, DependenciesTree, normalize
#from ppp_datamodel import Resource, Missing
import data

from unittest import TestCase

class StandardTripleTests(TestCase):

    def testAndNormalize(self):
        tree = computeTree(data.give_chief()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "intersection",
    "list": [
        {
            "subject": {
                "value": "chief",
                "type": "resource"
            },
            "type": "triple",
            "predicate": {
                "value": "identity",
                "type": "resource"
            },
            "object": {
                "type": "missing"
            }
        },
        {
            "subject": {
                "value": "prime minister",
                "type": "resource"
            },
            "type": "triple",
            "predicate": {
                "value": "identity",
                "type": "resource"
            },
            "object": {
                "type": "missing"
            }
        }
    ]
}
)

    def testSuperlativeNormalize(self):
        tree = computeTree(data.give_opera()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "list": [
        {
            "list": {
                "list": {
                    "value": "Gilbert",
                    "type": "resource"
                },
                "predicate": "default",
                "type": "sort"
            },
            "type": "first"
        },
        {
            "list": {
                "list": {
                    "value": "Sullivan opera",
                    "type": "resource"
                },
                "predicate": "default",
                "type": "sort"
            },
            "type": "first"
        }
    ],
    "type": "intersection"
}
)

    def testNormalize1(self):
        tree = computeTree(data.give_president_of_USA()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "object": {
        "type": "missing"
    },
    "subject": {
        "type": "resource",
        "value": "United States"
    },
    "predicate": {
        "type": "resource",
        "value": "president"
    },
    "type": "triple"
})

    def testNormalize2(self):
        tree = computeTree(data.give_LSD_LIB()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "intersection",
    "list": [
        {
            "object": {
                "type": "missing"
            },
            "predicate": {
                "value": "writer",
                "type": "resource"
            },
            "subject": {
                "value": "Lucy in the Sky with Diamonds",
                "type": "resource"
            },
            "type": "triple"
        },
        {
            "object": {
                "type": "missing"
            },
            "predicate": {
                "value": "Let It Be",
                "type": "resource"
            },
            "subject": {
                "value": "Lucy in the Sky with Diamonds",
                "type": "resource"
            },
            "type": "triple"
        }
    ]
})

    def testNormalize3(self):
        tree = computeTree(data.give_obama_president_usa()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "intersection",
    "list": [
        {
            "object": {
                "type": "missing"
            },
            "type": "triple",
            "predicate": {
                "value": "identity",
                "type": "resource"
            },
            "subject": {
                "value": "Obama",
                "type": "resource"
            }
        },
        {
            "object": {
                "value": "United States president",
                "type": "resource"
            },
            "type": "triple",
            "predicate": {
                "value": "identity",
                "type": "resource"
            },
            "subject": {
                "type": "missing"
            }
        }
    ]
})

    def testNormalizeR8(self):
        tree = computeTree(data.mistake()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "resource",
    "value": "mistake"
})

    def testNormalizeR3(self):
        tree = computeTree(data.king()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "intersection",
    "list": [
        {
            "predicate": {
                "value": "king",
                "type": "resource"
            },
            "subject": {
                "type": "missing"
            },
            "type": "triple",
            "object": {
                "value": "Louis XIV",
                "type": "resource"
            }
        },
        {
            "predicate": {
                "value": "Louis XIV",
                "type": "resource"
            },
            "subject": {
                "value": "France",
                "type": "resource"
            },
            "type": "triple",
            "object": {
                "type": "missing"
            }
        }
    ]
})