def validate_plate(plate):
    pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
    if not re.fullmatch(pattern, plate.upper()):
        raise ValueError(f'Некорректный знак: {plate}')
    return plate.upper()