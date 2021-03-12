import requests
import triyes


def start(url):
    if not url:
        print("\033[32mERRO: type a valid website\033[0m")
        pass
    try: 
        totry = triyes.factory()
        
        results  = {"y": [], "n": []}

        for item in totry:
            n_url = url + '/'+ item
            resp = requests.get(n_url)

            if resp.status_code == 404:
                print(f'\033[35mURL: {n_url}, exists: \033[31mNot!\033[0m, HTTP_code: {resp.status_code}')
            else:
                print(f'\033[35mURL: {n_url}, exists: \033[32mYes!\033[0m')
                results['y'].append(n_url)

        print('Valids urls:')
        print(results["y"])
            
    except:
        print("ERRO AO visitar!")