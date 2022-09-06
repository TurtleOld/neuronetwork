def hello_main():
    nv.set_default('listen', {'no_input_timeout': 4000,
                              'recognition_timeout': 30000,
                              'speech_complete_timeout': 1500,
                              'asr_complete_timeout': 2500})
    with nv.listen(500, entities=[
        'hello_null',
        'recommend_main',
        'hangup_wrong_time',
        'hello_repeat'
    ]) as result:
        pass
    return hello_logic(result)


def hello():
    nn.log('hello unit')
    nv.say('hello')
    return hello_main()


def hello_null():
    nn.log('hello null')
    nv.say('hello_null')
    return hello_main()


def hello_default():
    nn.log('hello default')
    nv.say('recommend_main')
    return recommended_main()


def hangup_wrong_time():
    nn.log('wrong_time')
    nv.say('hangup_wrong_time')
    return hangup_main()


def hello_repeat_say():
    nn.log('hello repeat')
    nv.say('hello_repeat')
    return hello_main()


def hello_logic(result):
    if not result:
        return hello_null()
    if not result.has_entities():
        return hello_default()
    if result.has_entity('recommend_main'):
        if result.entity('recommend_main') == 'true':
            nn.log('recommend_main unit')
            return hello_default()
    if result.has_entity('hello_repeat'):
        if result.entity('repeat') == 'true':
            nn.log('repeat unit')
            return hello_repeat_say()
    if result.has_entity('hangup_wrong_time'):
        if result.entity('hangup_wrong_time') == 'true':
            nn.log('hangup wrong time unit')
            return hangup_wrong_time()


def recommended_main():
    nv.set_default('listen', {'no_input_timeout': 4000,
                              'recognition_timeout': 30000,
                              'speech_complete_timeout': 1500,
                              'asr_complete_timeout': 2500})
    with nv.listen(500, entities=[
        'recommend_null',
        'recommend_default',
        'hangup_negative',
        'hangup_positive',
        'recommend_score_negative',
        'recommend_score_neutral',
        'recommend_score_positive',
        'recommend_repeat',
        'recommend_repeat_2',
        'forward'
    ]) as result:
        pass
    return main_logic(result)


def recommend_null():
    nn.log('recommend_null')
    nv.say('recommend_null')
    return recommended_main()


def recommend_default():
    nn.log('recommend default')
    nv.say('recommend_default')
    return recommended_main()


def recommend_score_negative():
    nn.log('recommend_score_negative')
    nv.say('recommend_score_negative')
    return recommended_main()


def recommend_score_neutral():
    nn.log('recommend_score_neutral')
    nv.say('recommend_score_neutral')
    return recommended_main()


def recommend_score_positive():
    nn.log('recommend_score_positive')
    nv.say('recommend_score_positive')
    return recommended_main()


def recommend_repeat():
    nn.log('recommend_repeat')
    nv.say('recommend_repeat')
    return recommended_main()


def recommend_repeat_2():
    nn.log('recommend_repeat_2')
    nv.say('recommend_repeat_2')
    return recommended_main()


def hangup_negative():
    nn.log('hangup_negative')
    nv.say('hangup_negative')
    return hangup_main()


def hangup_positive():
    nn.log('hangup_positive')
    nv.say('hangup_positive')
    return hangup_main()


def main_logic(result):
    if not result:
        nn.log('recommend_null')
        return recommend_null()
    if not result.has_entities():
        nn.log('recommend default')
        return recommend_default()
    if result.has_entity('hangup_negative'):
        if result.entity('hangup_negative') == 'true':
            nn.log('hangup_negative')
            return hangup_negative()
    if result.has_entity('hangup_positive'):
        if result.entity('hangup_positive') == 'true':
            nn.log('hangup_positive')
            return hangup_positive()
    if result.has_entity('recommend_score_negative'):
        if result.entity('recommend_score_negative') == 'true':
            nn.log('recommend_score_negative')
            return recommend_score_negative()
    if result.has_entity('recommend_score_positive'):
        if result.entity('recommend_score_positive') == 'true':
            nn.log('recommend_score_positive')
            return recommend_score_positive()
    if result.has_entity('recommend_score_neutral'):
        if result.entity('recommend_score_neutral') == 'true':
            nn.log('recommend_score_neutral')
            return recommend_score_neutral()
    if result.has_entity('recommend_repeat'):
        if result.entity('recommend_repeat') == 'true':
            nn.log('recommend_repeat')
            return recommend_repeat()
    if result.has_entity('recommend_repeat_2'):
        if result.entity('recommend_repeat_2') == 'true':
            nn.log('recommend_repeat_2')
            return recommend_repeat_2()
    if result.has_entity('forward'):
        if result.entity('forward') == 'true':
            nn.log('forward')
            return forward()


def hangup_main():
    nv.set_default('listen', {'no_input_timeout': 4000,
                              'recognition_timeout': 30000,
                              'speech_complete_timeout': 1500,
                              'asr_complete_timeout': 2500})
    with nv.listen(500, entities=[
        'hangup_positive',
        'hangup_negative',
        'hangup_wrong_time',
        'hangup_null',
    ]) as result:
        pass
    return hangup_logic(result)


def hangup_null():
    nn.log('hangup_null')
    nv.say('hangup_null')
    return hangup_main()


def hangup_logic(result):
    if not result:
        nn.log('hangup_null')
        nv.say('hangup_null')
        return hangup_null()
    if result.has_entity('hangup_positive'):
        if result.entity('hangup_positive') == 'true':
            nn.log('hangup_positive')
            return hangup_positive()
    if result.has_entity('hangup_negative'):
        if result.entity('hangup_negative') == 'true':
            nn.log('hangup_negative')
            return hangup_negative()
    if result.has_entity('hangup_wrong_time'):
        if result.entity('hangup_wrong_time') == 'true':
            nn.log('hangup_wrong_time')
            return hangup_wrong_time()


def forward():
    nn.log('forward')
    nv.say('forward')
    nn.dialog.entry_point = 'operator'
    return


def forward_logic(result):
    if result.has_entity('forward'):
        if result.entity('forward') == 'true':
            nn.log('forward')
            return forward()
