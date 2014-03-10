from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


class TocPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "m_cmsplugin_toc/table_of_contents.html"

plugin_pool.register_plugin(TocPlugin)