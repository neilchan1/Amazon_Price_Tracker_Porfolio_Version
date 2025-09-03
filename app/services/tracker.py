# PSEUDOCODE: Tracker service (Core logic)
#
# Responsibilities:
# - For a given Product record:
#     * fetch HTML via Fetcher
#     * parse via Parser
#     * store PriceHistory
#     * update Product.last_price_price, last_checked_at
#     * trigger notifier when conditions met
#
# Example (pseudocode):
#
# async def track_product(session, product):
#     html = await fetcher.get_html(product.url)
#     parsed = parser.parse(html)
#     if parsed.price:
#         add PriceHistory(product.id, parsed.price)
#         if parsed.price <= product.target_price:
#             await notifier.notify_price_drop(...)
#     commit transaction
