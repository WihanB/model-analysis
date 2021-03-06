# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility for Colab renderer API."""



import json
from IPython import display

from tensorflow_model_analysis.types_compat import Any, Dict, List, Text, Union


def render_component(
    component_name,
    data,
    config
):
  """Renders the specified component in Colab.

  Colab requires custom visualization to be rendered in a sandbox so we cannot
  use Jupyter widget.

  Args:
    component_name: The name of the component to render.
    data: A dictionary containing data for visualization.
    config: A dictionary containing the configuration.
  """
  display.display(
      display.HTML("""
          <link rel="import"
          href="/nbextensions/tfma_widget_js/vulcanized_template.html">
          <{component_name} id="component"></{component_name}>
          <script>
          const element = document.getElementById('component');
          element.config = JSON.parse('{config}');
          element.data = JSON.parse('{data}');
          </script>
          """.format(
              component_name=component_name,
              config=json.dumps(config),
              data=json.dumps(data))))
