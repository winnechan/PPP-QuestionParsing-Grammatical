import json

from ppp_questionparsing_grammatical import computeTree, simplify, DependenciesTree, QuotationHandler, normalize, GrammaticalError
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
                "predicate": {
                    "value": "default",
                    "type": "resource"
                },
                "list": {
                    "value": "Gilbert",
                    "type": "resource"
                },
                "type": "sort"
            },
            "type": "first"
        },
        {
            "list": {
                "predicate": {
                    "value": "default",
                    "type": "resource"
                },
                "list": {
                    "predicate": {
                        "value": "opera",
                        "type": "resource"
                    },
                    "object": {
                        "type": "missing"
                    },
                    "subject": {
                        "value": "Sullivan",
                        "type": "resource"
                    },
                    "type": "triple"
                },
                "type": "sort"
            },
            "type": "first"
        }
    ],
    "type": "intersection"
})

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
        handler = QuotationHandler('foo')
        sentence = 'Who wrote "Lucy in the Sky with Diamonds" and "Let It Be"?'
        nonAmbiguousSentence = handler.pull(sentence)
        result=data.give_LSD_LIB()
        tree=computeTree(result['sentences'][0])
        handler.push(tree)
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "list": [
        {
            "object": {
                "type": "missing"
            },
            "predicate": {
                "list": [
                    {
                        "value": "author",
                        "type": "resource"
                    },
                    {
                        "value": "writer",
                        "type": "resource"
                    }
                ],
                "type": "list"
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
                "list": [
                    {
                        "value": "author",
                        "type": "resource"
                    },
                    {
                        "value": "writer",
                        "type": "resource"
                    }
                ],
                "type": "list"
            },
            "subject": {
                "value": "Let It Be",
                "type": "resource"
            },
            "type": "triple"
        }
    ],
    "type": "intersection"
})

    def testNormalize3(self):
        tree = computeTree(data.give_obama_president_usa()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "intersection",
    "list": [
        {
            "type": "triple",
            "predicate": {
                "value": "instance of",
                "type": "resource"
            },
            "subject": {
                "type": "missing"
            },
            "object": {
                "value": "Obama",
                "type": "resource"
            }
        },
        {
            "type": "triple",
            "predicate": {
                "value": "identity",
                "type": "resource"
            },
            "subject": {
                "type": "missing"
            },
            "object": {
                "type": "triple",
                "predicate": {
                    "value": "president",
                    "type": "resource"
                },
                "subject": {
                    "value": "United States",
                    "type": "resource"
                },
                "object": {
                    "type": "missing"
                }
            }
        }
    ]
})

    def testNormalizeR8(self):
        tree = computeTree(data.mistake()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "subject": {
        "type": "resource",
        "value": "mistake"
    },
    "object": {
        "type": "missing"
    },
    "predicate": {
        "type": "list",
        "list": [
            {
                "type": "resource",
                "value": "place"
            },
            {
                "type": "resource",
                "value": "location"
            },
            {
                "type": "resource",
                "value": "residence"
            }
        ]
    },
    "type": "triple"
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

    def testNormalizeSuperl(self):
        tree = computeTree(data.tanzania()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "list": {
        "list": {
            "object": {
                "type": "missing"
            },
            "predicate": {
                "value": "mountain",
                "type": "resource"
            },
            "subject": {
                "value": "Tanzania",
                "type": "resource"
            },
            "type": "triple"
        },
        "predicate": {
                    "value" : "height",
                    "type"  : "resource"
                },
        "type": "sort"
    },
    "type": "last"
})

    def testNormalizeSuperl2(self):
        tree = computeTree(data.car()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "list": {
        "list": {
            "subject": {
                "value": "world",
                "type": "resource"
            },
            "predicate": {
                "value": "car",
                "type": "resource"
            },
            "object": {
                "type": "missing"
            },
            "type": "triple"
        },
        "predicate": {
                    "value" : "cost",
                    "type"  : "resource"
                },
        "type": "sort"
    },
    "type": "last"
})

    def testCop(self):
        tree = computeTree(data.black()['sentences'][0])
        self.assertRaises(GrammaticalError, lambda: simplify(tree))

    def testExists(self):
        tree = computeTree(data.king_england()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "list": {
        "predicate": {
            "type": "resource",
            "value": "king"
        },
        "subject": {
            "type": "resource",
            "value": "England"
        },
        "type": "triple",
        "object": {
            "type": "missing"
        }
    },
    "type": "exists"
})

    def testSemiQuestionWord1(self):
        tree = computeTree(data.roald()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "subject": {
        "value": "Roald Dahl",
        "type": "resource"
    },
    "type": "triple",
    "predicate": {
        "value": "book",
        "type": "resource"
    },
    "object": {
        "type": "missing"
    }
})

    def testSemiQuestionWord2(self):
        tree = computeTree(data.list_president1()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "object": {
        "type": "missing"
    },
    "predicate": {
        "value": "president",
        "type": "resource"
    },
    "type": "triple",
    "subject": {
        "value": "US",
        "type": "resource"
    }
})

    def testSemiQuestionWord3(self):
        tree = computeTree(data.list_president2()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "type": "triple",
    "object": {
        "type": "missing"
    },
    "predicate": {
        "type": "resource",
        "value": "president"
    },
    "subject": {
        "type": "resource",
        "value": "France"
    }
})

    def testSemiQuestionWord4(self):
        tree = computeTree(data.capital1()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "predicate": {
        "type": "resource",
        "value": "capital"
    },
    "type": "triple",
    "subject": {
        "type": "resource",
        "value": "France"
    },
    "object": {
        "type": "missing"
    }
})

    def testSemiQuestionWord5(self):
        tree = computeTree(data.capital2()['sentences'][0])
        qw = simplify(tree)
        result = normalize(tree)
        self.assertEqual(result,{
    "predicate": {
        "type": "resource",
        "value": "capital"
    },
    "type": "triple",
    "subject": {
        "type": "resource",
        "value": "France"
    },
    "object": {
        "type": "missing"
    }
})
