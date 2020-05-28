# filter

germs = ["bacteria", "viruses", "fungus"]

no_viruses = [x for x in germs if x != "viruses"]


# def is_virus(elem):
#     if elem != "viruses":
#         return True
#     else:
#         return False


def is_virus(elem):
    return elem != "viruses"


# filter - creates a new array
no_viruses_with_filter_method = filter(is_virus, germs)

print(list(no_viruses_with_filter_method))

no_viruses_filter_lambda = filter(lambda elem: elem != "viruses", germs)
print(tuple(no_viruses_filter_lambda))
