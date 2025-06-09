# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text.lower().strip()

        if user_input == "what can you do?":
            response = (
                "I can do the following:\n"
                "- Echo your message\n"
                "- Reverse your text\n"
                "- List my capabilities\n"
                "- Respond with a fallback if I don't understand you"
            )
        elif user_input.isalpha():
            reversed_text = user_input[::-1]
            response = f"Here's your message reversed: {reversed_text}"
        else:
            response = "Sorry, I didn't understand that."

        await turn_context.send_activity(MessageFactory.text(response))
