from alipay import AliPay
def pay(order_id,money):
    alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApWEWNqQ+VBaJt318LCZuBXaXXGvnT0tial+nh0kY0JCV3/fCFwCvA/sQ6WWccpq4Ao0K4U00Nk+AETC1ZXJkwzDxYGIA7pG8OmjyC7DQ+6vJWwVD8v+a1Y1K0EFMm6+x8r9aAZ4rY8cdxW1z9LSFaLiOVaelLxNAcmkITD1HfWjaIW9NBxFmbi6uxdQwQdycXhYiyTxmfL7cKIYmzQFIo4nCgfH1vK8t986gqEdIL+Id0H07aBU/UOeU/Ual9NuZxYFF2P/UxcN5jnj9TQ0pCWMc3XscCvg4V288sBnzQS21yUpIWzlADjAcLwMr5BryxJ0/pDsv2pv/nJTAgcAVdQIDAQAB
    -----END PUBLIC KEY-----'''

    app_private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEApWEWNqQ+VBaJt318LCZuBXaXXGvnT0tial+nh0kY0JCV3/fCFwCvA/sQ6WWccpq4Ao0K4U00Nk+AETC1ZXJkwzDxYGIA7pG8OmjyC7DQ+6vJWwVD8v+a1Y1K0EFMm6+x8r9aAZ4rY8cdxW1z9LSFaLiOVaelLxNAcmkITD1HfWjaIW9NBxFmbi6uxdQwQdycXhYiyTxmfL7cKIYmzQFIo4nCgfH1vK8t986gqEdIL+Id0H07aBU/UOeU/Ual9NuZxYFF2P/UxcN5jnj9TQ0pCWMc3XscCvg4V288sBnzQS21yUpIWzlADjAcLwMr5BryxJ0/pDsv2pv/nJTAgcAVdQIDAQABAoIBAGRtnsWz273IqfzpkRxmge2DZMtVI3R9vNgIGn4HH7CX/MuzcwPxAFcUgeKaN/VIi3HRIMhMz+YjRQwrXhyq6RG3iP0UxqgZjAqUbFg5Gc+bNH23ptnL6sTANqxc2x64BQH6vbe5y3OeGTApFX+GmHVNjfHqCl+Z+0r/CXDyzZUTuiPtnydlQHkJoSF3R8AvfW9BIUvaXKsD6AvjS35FZrHWSGPTfdJOQcgjpLWN1VO+xJN2levfcGiZrJ7Ux1j3B33ZZ6U6klRfHZCNh0ovfdS34KYu+z7Dks6Opg+BxcRybl9OhF5HAsw1+vq8DVb6bk5L6J+criqMDuaBbDNWYAECgYEA46yRTrKJpFW5qjVYQWMtS1fAO+UvDgiYma5/72laaPKCSDHyLvhgUvOgOyHUOqXbcx7SaTdKVeDR8aYJb1+BaroiFQd1hjMppK5ZGpA9hWHqpxIBmcsCIlN/nG4aQ/a83/ucqwyosyGX1RFP3Z+0FOd8bD1t/C4wOMsX1n6r1AECgYEAufRsww4Dyknlgg4bnjxVdQds6e76CCeSzrTFHFmSpNOKJVNouyn3bLWk8Ro2hH3KdOdyvyJ3FPj+M/3BF0JElJ7c6REHCR8aUHv2uAPLgm977MUIG5bLZx2D3XSZBuZZm89RtZCrObtAr3jXklRAwJqqmoqfQzGSbTKDcemkMXUCgYBHAS/EImxI4y9nRQHESsD6iWB7jYtyTf4Bl+lwaiP3LQKyr1j/ixjHZhGnv3In5EgfjBJFHChDxjzTp1uz7042UdyFQHFHrDclk/ZYEXoOWi5LcpMrOqPsvqvCxpfMcGwRUrBWrDkEvMpUefS1grQv/M3SGApwJpuFatmBXLoMAQKBgQCq9vygANyfOX2XKx1dSB9Rr3gFREABC1FAVpb6z6exfwP9+UfK/HSNMBvrx6vj+DsRbFHlROyzDZG5f03t8nFXKw/0AEG1szDgWnilCmgrDhCjySsBIozzywEXtEGVRGeShvOauN2UAIMiUTnxQSEfc5Py7gwrHQKA/vY23xakmQKBgDsFjwrNBzzWE5OaBhNuB0+4oBoa6ENN5+QCz/Kg8jtl1RFUAGlFd80FCdcuC/cvZ3/70nSMRVUvitWgTX8jtb1n1DLzxd/TeOwL4sfadPrQECSdjp38GZ7UaKxELyxPX6MAGlzy04tYfBlFJ7MbWlRlJdeOuN79KJIHjcpOJI6j
    -----END RSA PRIVATE KEY-----'''

    alipay=AliPay(
        appid="2016101500695594",
        app_notify_url="",
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
    )

    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=str(money),
        subject="商贸商城",
        return_url="http://127.0.0.1:8000/Buyer/index/",
        notify_url="http://127.0.0.1:8000/Buyer/index/",
    )

    return "https://openapi.alipaydev.com/gateway.do?" + order_string

if __name__ == '__main__':
    print(pay("100000006","10000"))