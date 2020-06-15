from random import choice, sample
from typing import Optional, List, Union

from .utilities import get_data


def name(count: Optional[int] = None,
         gender: Optional[str] = None) -> Union[str, List[str]]:
    '''Returns a random first name or a list of them
    :param count: The number of first names to be generated, defaults to `None`
    :type count: int, optional
    :param gender: Specifies the name of which gender will be generated, defaults to `None`
    :type gender: str, optional
    :returns: A random first name if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    if gender == 'm':
        names = get_data('names', 'male_names')
    elif gender == 'f':
        names = get_data('names', 'female_names')
    else:
        male_names = get_data('names', 'male_names')
        female_names = get_data('names', 'female_names')
        names = male_names + female_names

    if count:
        return sample(names, count)
    else:
        return choice(names)


def surname(count: Optional[int] = None) -> Union[str, List[str]]:
    '''Returns a random surname (or last name) or a list of them
    :param count: The number of surnames to be generated, defaults to `None`
    :type count: int, optional
    :returns: A surname if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    surnames = get_data('names', 'surnames')

    if count:
        return sample(surnames, count)
    else:
        return choice(surnames)


def fullname(count: Optional[int] = None,
             gender: Optional[str] = None) -> Union[str, List[str]]:
    '''Returns a random fullname or a list of them
    :param count: The number of fullnames to be generated, defaults to `None`
    :type count: int, optional
    :param gender: Specifies the fullname of which gender will be generated, defaults to `None`
    :type gender: str, optional
    :returns: A random fullname if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    if gender == 'm':
        names = get_data('names', 'male_names')
    elif gender == 'f':
        names = get_data('names', 'female_names')
    else:
        male_names = get_data('names', 'male_names')
        female_names = get_data('names', 'female_names')
        names = male_names + female_names

    surnames = get_data('names', 'surnames')

    if count:
        fullnames = []
        random_names = sample(names, count)
        random_surnames = sample(surnames, count)

        for name, surname in zip(random_names, random_surnames):
            fullnames.append(f'{name} {surname}')

        return fullnames
    else:
        return f'{choice(names)} {choice(surnames)}'


if __name__ == '__main__':
    print(name())
    print(surname())
    print(fullname())
