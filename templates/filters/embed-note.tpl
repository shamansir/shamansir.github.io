<section title="Embedded note"
  class="p-2 mx-2 mb-2 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-md shadow-inner">
  <header
    class="flex items-center justify-center text-l italic bg-${theme}-100 dark:bg-${theme}-950 text-${theme}-300 rounded py-1 px-2 mb-3">
    <a href="${ema:note:url}">
      <ema:note:title />
    </a>
  </header>
  <div>
    <apply template="/templates/components/pandoc" />
  </div>
</section>