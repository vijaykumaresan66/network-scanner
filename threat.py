COMMON_RISK_PORTS = {
    21: "FTP",
    23: "Telnet",
    445: "SMB",
    3389: "RDP",
    5900: "VNC"
}


def calculate_risk(device):

    ports = device.get("ports", [])

    score = 0

    for port in ports:

        if port in COMMON_RISK_PORTS:
            score += 2

    if device.get("vendor") == "Unknown":
        score += 1

    if score >= 6:
        return "🔴 High"

    elif score >= 3:
        return "🟡 Medium"

    return "🟢 Low"