(function(jQuery, $) {
	jQuery.fn.alarmcontrol = function(options) {
		options = jQuery.extend({}, jQuery.fn.alarmcontrol.options, options);
		var me = $(this);

		me.on('submit', function(event) {
			event.preventDefault()
		});

		var setAlarm = function() {
			var alarmTime = me.find('#set-alarm-value').val();
			var regexp = /^[0-9]{2}:[0-9]{2}$/;
			if (alarmTime.search(regexp) == -1) {
				alert('Please enter valid time in the format hh:mm');
				return;
			}
			var socketData = {
				target: 'alarm',
				type: 'wakeupTime',
				value: alarmTime
			};
			options.socket.send(JSON.stringify(socketData));
		};

		me.find('#set-alarm-button').on('click', setAlarm);
		me.on('submit', setAlarm);

		me.find('#alarm-select-music-button').on('click', function(event) {
			var music = me.find('.mpi3-select-music').val();
			var socketData = {
				target: 'alarm',
				type: 'wakeupMusic',
				value: music
			};
			options.socket.send(JSON.stringify(socketData));
		});
	};

	jQuery.fn.alarmcontrol.options = {
		socket: null
	}
})(jQuery, jQuery);
