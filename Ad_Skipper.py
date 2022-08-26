import base64

def main():
	banner()
	bypass()
	end()
	while True:
		process = input('Do you want to continue (yes/no) :: ')

		if (process == 'yes' or process == 'y' or process == 'Yes' or process == 'Y'):
			bypass()
			end()
			continue
		elif (process == 'no' or process == 'n' or process == 'No' or process == 'N'):
			break
		else:
			print('Enter either "yes" or "no") :: ')
	end()


def banner():
	print('\n')
	print('\t ==--==--==--==--==--==--==--==--==--==--==')
	print('\t ==--==--==--==--==--==--==--==--==--==--==')
	print('\t ==-- Channel Myanmar Movie Ad Skipper --==')
	print('\t ==--       Author : k4ung_k4ung       --==')
	print('\t ==--==--==--==--==--==--==--==--==--==--==')
	print('\t ==--==--==--==--==--==--==--==--==--==--==')
	print('\n')
	print('\t eg - Enter your movie link ::https://www.thecmpage.com/blah...')
	print('\n')

def bypass():
	url = input('\n Enter your movie link :: ')
	code = url.split("/?r=")[1]
	output_link = base64.b64decode(code)
	print('\n [#] Original Download Link is here :p >>> '+output_link.decode())
	
def end():
	print('\n----------------------------------------------------------------------------------------------------------------------\n')

if __name__ == '__main__':main()
