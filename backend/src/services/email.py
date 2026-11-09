from email_validator import validate_email, EmailNotValidError

def is_valido_dns(email:str) -> bool:
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailNotValidError:
        return False

