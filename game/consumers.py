from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class GameRoom(WebsocketConsumer):
    players = []

    cards = {}
    player_scores = {}
    stand = 0

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_code"]
        self.room_group_name = 'room_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # print()

        self.accept()
        self.send(text_data=json.dumps(
            {'event': "START",
             'status': 'connected',
             }))

    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    # From frontend to backend
    def receive(self, text_data=None, bytes_data=None):
        # Send message to room group
        response = json.loads(text_data)
        event = response.get("event", None)

        if event == "START":
            self.players.append(self.scope["user"].username)
            response["players"] = self.players
            response["players_connected"] = len(self.channel_layer.groups.get(self.room_group_name, {}).items())
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "START"
                }
            )
        if event == "HIT":
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "HIT"
                }
            )
        if event == "BLACKJACK":
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "BLACKJACK"
                }
            )
        if event == "STAND":
            self.stand = 1
            print(self.stand)
            self.player_scores = {}
            self.player_scores[response["player"]] = response["player-score"]
            print(self.player_scores)
            response["stand"] = self.stand
            response["scores"] = self.player_scores
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "STAND"
                }
            )
        if event == "PUSH":
            print(response)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "PUSH"
                }
            )
        if event == "WIN":
            print(response)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "WIN"
                }
            )
        if event == "LOSE":
            print(response)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "LOSE"
                }
            )
        if event == "PLACE_BET":
            self.cards = {}
            print(response)
            player_name = self.scope["user"].username
            self.cards[player_name] = response[player_name]
            print(self.cards)
            response["players_cards"] = self.cards
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps(response),
                    "event": "PLACE_BET"
                }
            )
            # python manage.py runserver
        if event == "DISCONNECT":
            player = response.get("player")
            self.players.remove(player)
            self.cards = {}
            self.player_scores = {}
            print(self.cards)
            response["players_cards"] = self.cards
            self.disconnect(code=0)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "run_game",
                    "payload": json.dumps({"player": player, "message": f"{player} disconnected"}),
                    "event": "DISCONNECTED"
                }
            )

    # Receive message from room group
    def run_game(self, res):
        # self.players.append(data["player"])
        # print(self.players)
        # Send message to WebSocket
        # backend to frontend
        self.send(text_data=json.dumps({
            "payload": res,
            # "players": self.p
        }))
