# time_return

a = int('3923910')


def make_readable(seconds: int):
    HH = str(seconds // 3600).zfill(2)
    MM = str(seconds % 3600 // 60).zfill(2)
    SS = str(seconds % 60).zfill(2)
    return (f'{HH}:{MM}:{SS}')


print(make_readable(a))
