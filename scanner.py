import nmap

begin = 0
end = 1500
target = '127.0.0.1'
scanner = nmap.PortScanner()

# Solo muestra el estado del puerto
for i in range(begin, end+1):
    results = scanner.scan(target, str(i))
    results = results['scan'][target]['tcp'][i]['state']
    print(f'Port {i} is {results}')
