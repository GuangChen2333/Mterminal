permission = 3
import os
PLUGIN_METADATA = {
	'id': 'mterminal',
	'version': '2021201',
	'name': 'Mterminal',
	'description': 'Add command to enable using terminal in minecraft',
	'author': 'Guang_Chen_',
	'link': 'https://github.com/GuangChen2333/Mterminal',
	'dependencies': {
		'mcdreforged': '>=1.0.0',
	}
}
def on_user_info(server, info):
	p = server.get_permission_level(info)
	t = info.content.split()
	if t[0] == '!!os':
		if p >= permission:
			command = info.content.split('!!os ')[1]
			result = os.popen(command)
			res = result.read()
			for line in res.splitlines():
				server.reply(info,line)