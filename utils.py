import json

from flask import Flask


def load_candidates():
    """
    load data from file
    :param file: filename in type = str
    :return:list with data
    """

    with open("candidates.json", 'r', encoding='utf-8') as f:
        return json.load(f)


def format_print(dct):
    """

    :param lst:
    :return:
    """
    res = f'Имя кандидата - {dct["name"]}\n' \
          f'Позиция кандидата - {dct["pk"]}\n' \
          f'Навыки - {dct["skills"]}\n\n'
    return res


def get_all():
    """
    print all candidates
    :param dict: dict with data about candidates
    :return: print views all candidates
    """
    res = '<pre>\n'
    for i in load_candidates():
        res += format_print(i)
    return res + '</pre>'


def get_by_pk(pk):
    """
    return name candidates by pk
    :param pk: int
    :return: name candidates(type dict)
    """
    for res in load_candidates():
        if res['pk'] == pk:
            return res



def get_by_name(name=str):
    """
    return name candidates with the name
    :param name: name type str
    :return: str with cadidates's data
    """
    res = []
    for i in load_candidates():
        if name.lower() in (i['name']).lower():
            res.append(i)
    return res


def get_by_skill(skill=str):
    """
    return скил candidates with the name
    :param skill: skill type str
    :return: str with cadidates's data
    """
    res = []
    print(skill)
    for i in load_candidates():
        if skill.lower() in (i['skills']).lower():
            res.append(i)
    return res
