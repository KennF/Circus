from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('report', 'templates'))
template = env.get_template('content.html')
entries = [{"title":"feature1", "text":1}, {"title":"feature2", "text":2}]
content = template.render(entries=entries)
with open('result.html', 'w+') as f:
    f.write(content)

