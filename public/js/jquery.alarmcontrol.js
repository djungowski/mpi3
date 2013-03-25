(function(jQuery, $) {
	jQuery.fn.alarmcontrol = function(options) {
		options = jQuery.extend({}, jQuery.fn.alarmcontrol.options, options);
		var me = $(this);

		me.on('submit', function(event) {
			event.preventDefault()
		});

		me.find('#stop-alarm').on('click', function(event) {
			var socketData = {
				target: 'alarm',
				type: 'stop'
			};
			options.socket.send(JSON.stringify(socketData));
		});

		me.find('#set-alarm-button').on('click', function(event) {
			var alarmTime = me.find('#set-alarm-value').val();
			var socketData = {
				target: 'alarm',
				type: 'wakeupTime',
				value: alarmTime
			};
			options.socket.send(JSON.stringify(socketData));
		});

		me.find('#alarm-select-music-button').on('click', function(event) {
			var music = me.find('#alarm-select-music').val();
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
