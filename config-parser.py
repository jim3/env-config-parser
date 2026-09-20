# Environment Config Parser

def parse_env_config(config_string: str) -> dict[str, str]:
    config = {}

    for l in config_string.splitlines():
        l = l.strip()
        if not l or l.startswith("#"):
            continue
        key, value = l.split("=", 1)
        config[key.strip()] = value.strip()

    return config
    

def main():
    print(parse_env_config("  HOST  =  localhost  \n  PORT  =  8080  "))
    print(parse_env_config("HOST=localhost\n\n\nPORT=8080\n"))
    print(parse_env_config("DEBUG=true\nTIMEOUT=30"))
    print(parse_env_config("  USER  =  admin  \n  MODE = production  "))
    print(parse_env_config("# Database settings\nDB_HOST=localhost\n\nDB_PORT=5432")) # {'DB_HOST': 'localhost', 'DB_PORT': '5432'}


if __name__ == "__main__":
    main()
