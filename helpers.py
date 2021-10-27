
def pagination_data(paginator,page):
    if paginator.num_pages ==1:
        return []
    left =[]
    right =[]
    left_has_more = False
    right_has_more = False
    first = False
    last = False

    try:
        page_number = int(page)
    except ValueError:
        page_number = 1
    except:
        page_number = 1

    total_pages = paginator.num_pages
    page_range = paginator.page_range

    if page_number == 1:
        right = page_range[page_number:page_number + 4]
        if right[-1] <total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True

    elif page_number == total_pages:
        left = page_range[(page_number - 3) if(page_number - 3) > 0 else 0: page_number - 1]

        if left[0] > 2:
            left_has_more = True

        if left[0] > 1:
            first = True

    else:
        left = page_range[(page_number - 3)if(page_number - 3) > 0 else 0: page_number - 1]
        right = page_range[page_number: page_number + 2]
        if right[-1] < total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True

        if left[0] > 2:
            left_has_more = True
        if left[0] > 1:
            first = True


    data = {
        'left' :left,
        'right': right,
        'left_has_more':left_has_more,
        'right_has_more': right_has_more,
        'first': first,
        'last':last

    }
    return data
