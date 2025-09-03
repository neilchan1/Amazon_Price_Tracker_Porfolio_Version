"""
Discord notifier example (Code snippet).
"""
import httpx
from typing import Optional

async def send_discord_notification(webhook_url: str, content: str) -> None:
    """Send a simple message payload to a Discord webhook.

    Note: In production, handle retries, rate-limiting, and logging.
    """
    if not webhook_url:
        raise ValueError("webhook_url is required")

    async with httpx.AsyncClient(timeout=10.0) as client:
        await client.post(webhook_url, json={"content": content})

async def notify_price_drop(product_title: str, product_url: str, old_price: Optional[int], new_price: int, currency: str, webhook_url: str):
    old = f"{old_price/100:.2f}" if old_price is not None else "N/A"
    new = f"{new_price/100:.2f}"
    content = (
        f"**Price Drop**\n{product_title}\n{product_url}\nOld: {old} {currency} → New: {new} {currency}"
    )
    await send_discord_notification(webhook_url, content)
