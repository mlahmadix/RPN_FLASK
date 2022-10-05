from rpn.namespace import StackList, OpList, OPS


def test_get_list_route():
    ret = StackList().get()
    assert ret == {}


def test_post_route():
    ret, code_status = StackList().post()
    assert code_status == 201


def test_op_list_route():
    operators = OpList().get()
    assert operators == {"operators": list(OPS.keys())}
