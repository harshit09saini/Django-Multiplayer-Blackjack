// Generate a random room code and pre-populate the room code field if create room is selected

$(document).ready(function () {
    $('#id_room_choice').change(function () {
        const genRanHex = size => [...Array(size)].map(() => Math.floor(Math.random() * 16).toString(16)).join('');

        let room_choice = $("#id_room_choice").val();
        if (room_choice == "Create Room") {
            random_room_code = genRanHex(8)
            $('#id_room_code').val(random_room_code);
        }
    })
});

