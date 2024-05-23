def clean_value(value):
    val_cleaned = value.replace("'", "''")
    val_cleaned = val_cleaned.replace("\"", "\\\"")

    return val_cleaned
