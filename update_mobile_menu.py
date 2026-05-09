from pathlib import Path

root = Path('.')

menu_button_block = '''                <!-- Mobile Menu Button -->
                <button id="mobileMenuButton" class="lg:hidden p-2">
                    <i class="ti ti-menu-2 text-2xl"></i>
                </button>

                <!-- Mobile Menu Panel -->
                <div id="mobileMenuPanel" class="fixed inset-0 z-40 hidden lg:hidden">
                    <div class="absolute inset-0 bg-black/30 backdrop-blur-sm" data-close-mobile-menu></div>
                    <div class="relative h-full w-full max-w-sm bg-white shadow-2xl overflow-y-auto">
                        <div class="flex items-center justify-between border-b border-gray-200 px-5 py-4">
                            <a href="index.html" class="flex items-center gap-2">
                                <img src="img/logo_v.svg" alt="Visium Digital" class="h-8">
                                <span class="font-semibold text-gray-900">Visium Digital</span>
                            </a>
                            <button id="mobileMenuClose" class="p-2">
                                <i class="ti ti-x text-2xl"></i>
                            </button>
                        </div>
                        <nav class="px-5 py-6 space-y-4 text-base">
                            <a href="el_instituto.html" class="block text-gray-800 hover:text-gray-900">La Academia</a>
                            <div class="space-y-2">
                                <p class="text-xs uppercase tracking-[0.18em] text-gray-400">Negocios y Finanzas</p>
                                <a href="economia_digital.html" class="block text-gray-600 hover:text-gray-900">Economía Digital</a>
                                <a href="digital_empower.html" class="block text-gray-600 hover:text-gray-900">Digital Empower</a>
                                <a href="edufintech.html" class="block text-gray-600 hover:text-gray-900">Edufintech</a>
                                <a href="economia_digital.html" class="block text-gray-600 hover:text-gray-900">Mercados Financieros</a>
                            </div>
                            <div class="space-y-2">
                                <p class="text-xs uppercase tracking-[0.18em] text-gray-400">Diseño y Desarrollo</p>
                                <a href="ui_para_graficos.html" class="block text-gray-600 hover:text-gray-900">Diseño UI: Balance Funcional</a>
                                <a href="html_css_graficos.html" class="block text-gray-600 hover:text-gray-900">HTML & CSS para Creativos</a>
                                <a href="diseno_maquetado_ia.html" class="block text-gray-600 hover:text-gray-900">Diseño y Maquetado con IA</a>
                                <a href="diseno_productos.html" class="block text-gray-600 hover:text-gray-900">Diseño de Productos</a>
                            </div>
                            <a href="blog_t.html" class="block text-gray-800 hover:text-gray-900 font-medium">Biblioteca</a>
                        </nav>
                        <div class="border-t border-gray-200 px-5 py-5">
                            <a href="iniciar_estudios.html" class="block w-full rounded-full bg-gray-900 text-white text-center py-3 font-semibold hover:bg-gray-800">Consulta</a>
                        </div>
                    </div>
                </div>
            </nav>'''

script_snippet = '''<script>
  document.addEventListener('DOMContentLoaded', function () {
    var openBtn = document.getElementById('mobileMenuButton');
    var closeBtn = document.getElementById('mobileMenuClose');
    var panel = document.getElementById('mobileMenuPanel');
    var overlay = document.querySelector('[data-close-mobile-menu]');
    function toggleMenu() {
      if (!panel) return;
      panel.classList.toggle('hidden');
    }
    openBtn?.addEventListener('click', toggleMenu);
    closeBtn?.addEventListener('click', toggleMenu);
    overlay?.addEventListener('click', toggleMenu);
  });
</script>\n'''

modified = []
for path in sorted(root.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if '<!-- Mobile Menu Button -->' not in text:
        continue
    if 'id="mobileMenuPanel"' in text:
        continue
    new_text = text.replace(
        '                <!-- Mobile Menu Button -->\n                <button class="lg:hidden p-2">\n                    <i class="ti ti-menu-2 text-2xl"></i>\n                </button>\n            </nav>',
        menu_button_block,
    )
    if new_text == text:
        continue
    if '</body>' in new_text and script_snippet not in new_text:
        new_text = new_text.replace('</body>', script_snippet + '</body>')
    path.write_text(new_text, encoding='utf-8')
    modified.append(str(path))

print('Modified files:')
for m in modified:
    print(m)
