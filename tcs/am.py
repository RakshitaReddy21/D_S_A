def secureMaximumDeliveries(deliveryLogs, k):
    h = k // 2
    ans = 0
    maxDelivery = max(deliveryLogs, default=0)

    for t in range(1, maxDelivery + 1):
        freeWarehouses = 0
        extraCosts = []

        for delivery in deliveryLogs:
            q, r = divmod(delivery, t)
            freeWarehouses += q
            extraCosts.append(t - r)

        extra = max(0, k - freeWarehouses)

        if extra == 0:
            cost = 0
        else:
            extraCosts.sort()
            if extra <= len(extraCosts):
                cost = sum(extraCosts[:extra])
            else:
                cost = sum(extraCosts) + (extra - len(extraCosts)) * t

        secure = h * t - cost
        ans = max(ans, secure)

    return ans
