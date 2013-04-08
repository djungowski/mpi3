(function(jQuery, $) {
	jQuery.fn.musiccontrol = function(options) {
		var baseOptions,
			me,
			getMusic;

		options = jQuery.extend({}, jQuery.fn.musiccontrol.options, options);
		baseOptions = {
			target: 'player'
		};
		me = $(this);

		var getMusic = function() {
			return $('.mpi3-select-music').val();
		};

		me.find('.mpi3-music-play').on('click', function(event) {
			var music;

			music = getMusic();
			playOptions = {
				value: music,
				type: 'play'
			};
			playOptions = jQuery.extend(baseOptions, playOptions);
			options.socket.send(JSON.stringify(playOptions));
		});

		me.find('.mpi3-music-pause').on('click', function(event) {
			var music;

			music = getMusic();
			playOptions = {
				type: 'pause'
			};
			playOptions = jQuery.extend(baseOptions, playOptions);
			options.socket.send(JSON.stringify(playOptions));
		});

		me.find('.mpi3-music-stop').on('click', function(event) {
			var music;

			music = getMusic();
			playOptions = {
				type: 'stop'
			};
			playOptions = jQuery.extend(baseOptions, playOptions);
			options.socket.send(JSON.stringify(playOptions));
		});
	};

	jQuery.fn.musiccontrol.options = {
		socket: null
	};
})(jQuery, jQuery);