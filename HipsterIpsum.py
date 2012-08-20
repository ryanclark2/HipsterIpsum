import sublime, sublime_plugin
import random

class HipsterIpsumCommand(sublime_plugin.TextCommand):
    def run(self, edit, qty = 10):
        selections = self.view.sel()
        for selection in selections:
            # always start with Fixie mustache
            para = "Fixie mustache ";
            # words from hipsteripsum.com
            words = "Selvage laboris cardigan messenger bag, brooklyn put a bird on it mollit mixtape reprehenderit sapiente accusamus american apparel ethnic ea. Adipisicing fixie viral quinoa. Authentic sustainable do, vegan laborum cillum duis. Voluptate accusamus nostrud, deserunt assumenda tofu etsy. Cardigan wes anderson viral portland terry richardson semiotics, small batch 8-bit nostrud chillwave bushwick bicycle rights iphone. Street art est pop-up, hella salvia nihil sed gluten-free seitan ennui helvetica. Semiotics exercitation placeat odio, before they sold out 3 wolf moon Austin. Cillum pinterest bespoke, tofu single-origin coffee pariatur freegan artisan echo park letterpress. Incididunt aliqua velit mcsweeney's yr. Dolor organic anim, single-origin coffee bespoke yr letterpress fixie. Sartorial beard do VHS non, craft beer street art laboris fixie photo booth placeat. Eu sint bicycle rights craft beer letterpress food truck. Esse gentrify cupidatat, banh mi kogi labore id terry richardson pinterest. Tempor dreamcatcher semiotics selvage sint polaroid, before they sold out sartorial brunch officia labore wayfarers terry richardson vero banksy. Tattooed Austin godard, vero butcher master cleanse authentic carles brooklyn officia. Excepteur swag retro fap officia, consequat quis small batch tofu sustainable nostrud. Lomo high life cred direct trade, exercitation est leggings keytar swag farm-to-table ethnic chambray. Master cleanse readymade est single-origin coffee aliqua, marfa consequat nesciunt seitan proident magna. Proident farm-to-table fingerstache, nostrud consectetur mumblecore ennui single-origin coffee anim bespoke messenger bag. Irony cardigan enim, lo-fi odio chillwave keffiyeh dolor. Synth VHS truffaut, you probably haven't heard of them sriracha farm-to-table semiotics hella delectus pariatur incididunt stumptown small batch readymade. Chambray selvage pariatur duis nihil trust fund. Adipisicing etsy blog ullamco. Selvage salvia sunt seitan. Tumblr est consectetur magna, next level nesciunt ex portland pariatur laboris assumenda small batch. Nisi mcsweeney's sartorial qui vegan. Small batch irure retro flexitarian, beard tumblr bespoke voluptate art party gastropub fap excepteur organic umami salvia. Delectus 8-bit sartorial dolore dreamcatcher, synth umami irony keytar".split()

            from random import choice
            for x in range(random.randint(qty - qty/2, qty + qty/2)):
                para += choice(words) + " "
            para += choice(words) + ". "
            editor = self.view.begin_edit()

            # erase region
            self.view.erase(editor, selection)
            # insert para before current cursor position
            self.view.insert(editor, selection.begin(), para)

            # insert para over the top of selection, but remaining selected (not behavior we want)
            # self.view.replace(editor, self.view.sel()[0], para)

            self.view.end_edit(editor)