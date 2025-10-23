from livereload import Server, shell

# Serve the current directory
server = Server()

# Watch for changes in HTML, CSS, and JS files
server.watch('*.html')
server.watch('*.css')
server.watch('*.js')

# Serve on http://localhost:5500 by default
server.serve(root='.', port=5500)
