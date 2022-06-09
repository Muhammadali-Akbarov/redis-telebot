from environs import Env


class Environs:
    __BOT = 'bot'
    __REDIS = 'redis'
    __REDIS_CHARSET = 'utf-8'
    __REDIS_DECODE_RESPONSES=True
    
    def __init__(self):
        self.read_env = Env()
        self.read_env.read_env()

    def get(self, client_type: str) -> dict:
        env_dict: dict = {}

        if client_type == self.__BOT:
            env_dict['api_host'] = self.read_env('TELEGRAM_API_HOST')
            env_dict['api_token'] = self.read_env('TELEGRAM_API_TOKEN')
        
        if client_type == self.__REDIS:
            env_dict['host'] = self.read_env('REDIS_HOST')
            env_dict['port'] = self.read_env('REDIS_PORT')
            env_dict['db'] = 0
            
            env_dict['charset'] = self.__REDIS_CHARSET
            env_dict['decode_responses'] = self.__REDIS_DECODE_RESPONSES


        return env_dict

get_env = Environs()