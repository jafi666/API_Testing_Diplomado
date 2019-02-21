from compare import expect


@given(u'I have connection to host {url}')
def step_impl(context, url):
    expect(context.host).to_equal(url)


@when(u'I {method}')
def step_impl(context, method):
    expect(method).to_equal(context.method)


@then(u'I receive status code {code:d}')
def step_impl(context, code):
    expect(code).to_equal(context.code)
