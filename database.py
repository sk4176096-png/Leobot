from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL, DB_NAME


class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.db = self.client[DB_NAME]

        # Collections
        self.users = self.db.users
        self.messages = self.db.messages
        self.settings = self.db.settings

    async def save_message(self, user_id: str, role: str, content: str):
        """Save chat message"""
        await self.messages.insert_one({
            "user_id": user_id,
            "role": role,
            "content": content,
        })

    async def get_history(self, user_id: str, limit: int = 20):
        """Get last messages of a user"""
        cursor = (
            self.messages.find({"user_id": user_id})
            .sort("_id", -1)
            .limit(limit)
        )

        history = []

        async for msg in cursor:
            history.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        history.reverse()
        return history

    async def register_user(self, user_id: str, username: str):
        await self.users.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "username": username
                }
            },
            upsert=True
        )


db = Database()