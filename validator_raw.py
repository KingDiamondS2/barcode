from cerberus import Validator
body = {
    "data": {
        "ele1": 123.34,
        "ele2": "hello",
        "ele3": "321",
    }
}

body_validator = Validator({
    "data":{
        "type": "dict",
        "schema":{
            "ele1": { "type": "float", "required": True, "empty": False},
            "ele2": { "type": "string", "required": True, "empty": True},
            "ele3": { "type": "string", "required": True, "empty": False},
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print(f"resp: {response}")

