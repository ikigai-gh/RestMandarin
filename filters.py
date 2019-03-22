def _get_predicate(field, filter, value):
    if filter == 'exact':
        return field == value
    elif filter == 'notexact':
        return field != value
    elif filter == 'gt':
        return field > value
    elif filter == 'lt':
        return field < value
    elif filter == 'gte':
        return field >= value
    elif filter == 'lte':
        return field <= value
    elif filter == 'in' and isinstance(value, list):
        return field.in_(value)
    else:
        return None


def parse_filters(cls_model, req_params):
    filters = []
    for param, value in req_params.items():
        if '__' in param:
            filter = param.split('__')[1].split('=')[0]
            field = param.split('__')[0]
            p = _get_predicate(getattr(cls_model, field), filter, value)
            if p is not None:
                filters.append(p)
    return filters
