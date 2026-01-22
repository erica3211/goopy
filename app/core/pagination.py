from math import ceil
from sqlalchemy.orm import Query


def paginate(
    query: Query,
    page: int,
    size: int
):
    total = query.count()

    items = (
        query
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )

    total_pages = ceil(total / size) if total > 0 else 0

    return {
        "items": items,
        "page": page,
        "size": size,
        "total": total,
        "total_pages": total_pages
    }