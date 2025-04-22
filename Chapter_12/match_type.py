def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 200:
            return "Internet Server Error"
        case _:
            "Unknown status"
            
print(http_status(200))
