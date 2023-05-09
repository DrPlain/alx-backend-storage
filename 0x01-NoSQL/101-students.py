#!/usr/bin/env python3
""" Top students sorted in descending order of avg score """


def top_students(mongo_collection):
    """ Returns all students sorted by average """
    results = mongo_collection.aggregate([
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])

    return results
