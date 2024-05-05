browser.open('https://school.qa.guru')
browser.element('[name="lg"]').type('a.b@tele2.kz').press_enter()
browser.element('[name="pw"]').type('+++++').press_enter().press_enter()
browser.element('[class="page-header"]').should(have.text('Список тренингов'))