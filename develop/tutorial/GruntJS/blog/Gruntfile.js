module.exports = function(grunt){
    grunt.initConfig({
        uglify: {
            build: {
                src: ['js/app.js'],
                dest: 'js/app.min.js'
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.registerTask('default', ['uglify']);
    grunt.registerTask('test', 'log some stuff', function(){
        grunt.log.write('Log some stuff...').ok();
    });
};
