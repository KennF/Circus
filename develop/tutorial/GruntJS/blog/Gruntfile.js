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
};
